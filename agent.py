import DQN_implementation as dqn

identifier = "FEH MLP agent"

# start training
dqn.main(identifier=identifier, model_name="MLP", max_iteration=1000, epsilon=1,
         epsilon_decay=4.5e-4, epsilon_min=0.05, interval_iteration=10, gamma=1, test_size=50,
         learning_rate=0.0001, use_replay_memory=True, memory_size=50000, burn_in=10000)