

class Config:
	##Agent type
    agent_type="FCN" #FCN or CNN
    hidden_units= 512
    ## Frames
    skip_frames = 2
    history_length = 2
    ## Optimzation
    lr=0.005
    batch_size = 256
    n_minibatches = 200000
    ## testing
    n_test_episodes = 15
    rendering = True
   
