// TussiesJack - Blackjack Type Definitions

export enum Suit {
  SPADES = 'SPADES',
  HEARTS = 'HEARTS',
  DIAMONDS = 'DIAMONDS',
  CLUBS = 'CLUBS',
}

export enum Rank {
  TWO = '2',
  THREE = '3',
  FOUR = '4',
  FIVE = '5',
  SIX = '6',
  SEVEN = '7',
  EIGHT = '8',
  NINE = '9',
  TEN = '10',
  JACK = 'J',
  QUEEN = 'Q',
  KING = 'K',
  ACE = 'A',
}

export interface Card {
  suit: Suit;
  rank: Rank;
}

export interface GameState {
  playerCards: Card[];
  dealerCards: Card[];
  playerScore: number;
  dealerScore: number;
  playerHasAce: boolean;
  dealerHasAce: boolean;
  status: 'playing' | 'stand' | 'bust' | 'blackjack' | 'complete';
  result?: 'win' | 'loss' | 'push';
}

export interface GameAction {
  type: 'hit' | 'stand' | 'double' | 'split';
  confidence?: number;
  explanation?: string;
}

export interface PlayerStats {
  totalHands: number;
  wins: number;
  losses: number;
  pushes: number;
Create backend types definitions  totalBet: number;
  totalWinnings: number;
}#!/usr/bin/env python3
"""
TussiesJack - Blackjack Strategy Training
Trains a DQN model on simulated blackjack games using synthetic data.
The model learns optimal play from millions of simulated hands.
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import random
from collections import deque
import json
import os

# ==================== Blackjack Simulator ====================
class BlackjackSimulator:
    """Simulates blackjack games for training data generation."""
    
    ACTIONS = ['hit', 'stand', 'double']  # 0, 1, 2
    
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.reset_deck()
    
    def reset_deck(self):
        """Reset shoe with specified number of decks."""
        self.deck = [i % 13 for i in range(52 * self.num_decks)]
        random.shuffle(self.deck)
    
    def card_value(self, card):
        """Get blackjack value of a card (0=Ace, 1-8=2-9, 9-11=10,J,Q,K)."""
        if card == 0:  # Ace
            return 11
        elif card >= 9:
            return 10
        else:
            return card + 2
    
    def hand_value(self, cards):
        """Calculate best value of hand, accounting for Aces."""
        value = sum(self.card_value(c) for c in cards)
        aces = sum(1 for c in cards if c == 0)
        
        while value > 21 and aces > 0:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1
        
        return value
    
    def is_bust(self, cards):
        return self.hand_value(cards) > 21
    
    def play_hand(self, player_cards, dealer_upcard, policy_fn):
        """
        Simulate a single blackjack hand using a policy function.
        Returns: (final_player_cards, final_dealer_cards, reward)
        """
        dealer_cards = [dealer_upcard]
        
        # Player hits until stands or busts
        while True:
            player_value = self.hand_value(player_cards)
            dealer_value = self.card_value(dealer_upcard)
            
            # Get action from policy
            state = self.encode_state(player_cards, dealer_upcard)
            action = policy_fn(state)
            
            if action == 0:  # Hit
                if not self.deck:
                    self.reset_deck()
                player_cards.append(self.deck.pop())
                if self.is_bust(player_cards):
                    return player_cards, dealer_cards, -1.0  # Loss
            else:  # Stand or Double
                break
        
        # Dealer plays (hits on soft 17)
        while self.hand_value(dealer_cards) < 17:
            if not self.deck:
                self.reset_deck()
            dealer_cards.append(self.deck.pop())
        
        # Determine winner
        player_value = self.hand_value(player_cards)
        dealer_value = self.hand_value(dealer_cards)
        
        if dealer_value > 21:
            return player_cards, dealer_cards, 1.0  # Player wins
        elif player_value > dealer_value:
            return player_cards, dealer_cards, 1.0
        elif player_value == dealer_value:
            return player_cards, dealer_cards, 0.0  # Push
        else:
            return player_cards, dealer_cards, -1.0  # Loss
    
    def encode_state(self, player_cards, dealer_upcard):
        """Encode game state as feature vector."""
        player_value = self.hand_value(player_cards)
        dealer_value = self.card_value(dealer_upcard)
        has_ace = any(c == 0 for c in player_cards)
        can_split = len(player_cards) == 2 and player_cards[0] == player_cards[1]
        
        return np.array([
            player_value / 21.0,       # Normalized player value
            dealer_value / 11.0,       # Normalized dealer value
            float(has_ace),            # Has Ace
            float(can_split),          # Can split
            len(player_cards) / 5.0,   # Hand size (normalized)
        ], dtype=np.float32)

# ==================== DQN Agent ====================
class DQNAgent:
    """Deep Q-Network agent for learning blackjack strategy."""
    
    def __init__(self, state_size=5, action_size=3):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=10000)
        self.gamma = 0.99  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.learning_rate = 0.001
        
        # Build Q-network
        self.q_network = self._build_model()
        self.target_network = self._build_model()
        self.update_target_network()
    
    def _build_model(self):
        """Build neural network model."""
        model = keras.Sequential([
            layers.Input(shape=(self.state_size,)),
            layers.Dense(128, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=self.learning_rate),
                     loss='mse')
        return model
    
    def update_target_network(self):
        """Update target network weights."""
        self.target_network.set_weights(self.q_network.get_weights())
    
    def remember(self, state, action, reward, next_state, done):
        """Store experience in replay memory."""
        self.memory.append((state, action, reward, next_state, done))
    
    def act(self, state):
        """Choose action using epsilon-greedy policy."""
        if np.random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        q_values = self.q_network.predict(np.array([state]), verbose=0)
        return np.argmax(q_values[0])
    
    def replay(self, batch_size):
        """Train on batch from replay memory."""
        if len(self.memory) < batch_size:
            return
        
        batch = random.sample(self.memory, batch_size)
        states = np.array([x[0] for x in batch])
        actions = np.array([x[1] for x in batch])
        rewards = np.array([x[2] for x in batch])
        next_states = np.array([x[3] for x in batch])
        dones = np.array([x[4] for x in batch])
        
        # Predict Q-values
        target_q_values = self.q_network.predict(states, verbose=0)
        next_q_values = self.target_network.predict(next_states, verbose=0)
        
        for i in range(batch_size):
            if dones[i]:
                target_q_values[i][actions[i]] = rewards[i]
            else:
                target_q_values[i][actions[i]] = rewards[i] + self.gamma * np.max(next_q_values[i])
        
        self.q_network.fit(states, target_q_values, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# ==================== Training Function ====================
def train_dqn_agent(num_episodes=1000, batch_size=32):
    """Train DQN agent on simulated blackjack games."""
    
    print("\n" + "="*60)
    print("TussiesJack - Blackjack Strategy Training")
    print("="*60)
    
    simulator = BlackjackSimulator(num_decks=1)
    agent = DQNAgent(state_size=5, action_size=3)
    
    episode_rewards = []
    
    for episode in range(num_episodes):
        # Start new hand
        player_cards = [simulator.deck.pop()]
        dealer_upcard = simulator.deck.pop()
        
        state = simulator.encode_state(player_cards, dealer_upcard)
        episode_reward = 0
        
        # Play hand
        for step in range(20):  # Max 20 steps per hand
            action = agent.act(state)
            
            if action == 0:  # Hit
                if not simulator.deck:
                    simulator.reset_deck()
                player_cards.append(simulator.deck.pop())
                next_state = simulator.encode_state(player_cards, dealer_upcard)
                
                if simulator.is_bust(player_cards):
                    reward = -1.0
                    done = True
                else:
                    reward = 0.0
                    done = False
            else:  # Stand
                # Complete dealer hand
                dealer_cards = [dealer_upcard]
                while simulator.hand_value(dealer_cards) < 17:
                    if not simulator.deck:
                        simulator.reset_deck()
                    dealer_cards.append(simulator.deck.pop())
                
                # Calculate final reward
                player_value = simulator.hand_value(player_cards)
                dealer_value = simulator.hand_value(dealer_cards)
                
                if dealer_value > 21:
                    reward = 1.0
                elif player_value > dealer_value:
                    reward = 1.0
                elif player_value == dealer_value:
                    reward = 0.0
                else:
                    reward = -1.0
                
                next_state = simulator.encode_state(player_cards, dealer_upcard)
                done = True
            
            agent.remember(state, action, reward, next_state, done)
            episode_reward += reward
            state = next_state
            
            if done:
                break
        
        episode_rewards.append(episode_reward)
        agent.replay(batch_size)
        
        # Print progress
        if (episode + 1) % 100 == 0:
            avg_reward = np.mean(episode_rewards[-100:])
            print(f"Episode {episode+1}/{num_episodes} | Avg Reward: {avg_reward:.3f} | Epsilon: {agent.epsilon:.3f}")
    
    return agent, episode_rewards

# ==================== Model Export ====================
def export_to_tflite(agent, output_path='models/tussiesjack.tflite'):
    """Export trained model to TensorFlow Lite format."""
    
    print(f"\nExporting model to TensorFlow Lite...")
    
    # Create concrete function
    concrete_func = tf.function(lambda x: agent.q_network(x))
    concrete_func = concrete_func.get_concrete_function(tf.TensorSpec([1, 5], tf.float32))
    
    # Convert to TFLite
    converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    
    # Save model
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(tflite_model)
    
    print(f"✓ Model saved to {output_path}")
    print(f"  Model size: {len(tflite_model) / 1024:.1f} KB")

# ==================== Main ====================
if __name__ == '__main__':
    # Train agent
    agent, rewards = train_dqn_agent(num_episodes=1000, batch_size=32)
    
    # Export to TFLite
    export_to_tflite(agent, 'models/tussiesjack.tflite')
    
    # Save training stats
    stats = {
        'episodes': len(rewards),
        'final_avg_reward': float(np.mean(rewards[-100:])),
        'max_reward': float(np.max(rewards)),
        'min_reward': float(np.min(rewards))
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/training_stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Training Complete!")
    print(f"Final Average Reward: {stats['final_avg_reward']:.3f}")
    print(f"{'='*60}\n")


export interface HandHistory {
  id: string;
  userId: string;
  timestamp: number;
  playerCards: Card[];
  dealerCards: Card[];
  playerAction: GameAction;
  aiRecommendation: GameAction;
  result: 'win' | 'loss' | 'push';
  betAmount: number;
  winAmount: number;
}

export interface BasicStrategyInput {
  playerScore: number;
  dealerScore: number;
  hasAce: boolean;
  canSplit: boolean;
}

export interface StrategyOutput {
  action: 'hit' | 'stand' | 'double' | 'split';
  confidence: number;
}
