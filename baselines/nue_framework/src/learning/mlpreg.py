from sklearn.neural_network import MLPRegressor

class MLPReg(MLPRegressor):
    
    def __init__(self, n_layers = 1, n_hidden = 100, activation="relu",
                 solver='adam', alpha=0.0001,
                 batch_size='auto', learning_rate="constant",
                 learning_rate_init=0.001,
                 power_t=0.5, max_iter=200, shuffle=True,
                 random_state=None, tol=1e-4,
                 verbose=False, warm_start=False, momentum=0.9,
                 nesterovs_momentum=True, early_stopping=False,
                 validation_fraction=0.1, beta_1=0.9, beta_2=0.999,
                 epsilon=1e-8, n_iter_no_change=10, max_fun=15000):
        
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        
        hidden_layer_sizes = tuple( [ n_hidden for i in range(n_layers) ] )
        
        super().__init__( hidden_layer_sizes=hidden_layer_sizes,
            activation=activation, solver=solver, alpha=alpha,
            batch_size=batch_size, learning_rate=learning_rate,
            learning_rate_init=learning_rate_init, power_t=power_t,
            max_iter=max_iter, shuffle=shuffle,
            random_state=random_state, tol=tol, verbose=verbose,
            warm_start=warm_start, momentum=momentum,
            nesterovs_momentum=nesterovs_momentum,
            early_stopping=early_stopping,
            validation_fraction=validation_fraction,
            beta_1=beta_1, beta_2=beta_2, epsilon=epsilon,
            n_iter_no_change=n_iter_no_change, max_fun=max_fun )
    
    
    def set_params(self, **params):
        if not params:
            # Simple optimization to gain speed (inspect is slow)
            return self
        
        self.n_layers = params["n_layers"]
        self.n_hidden = params["n_hidden"]
        hidden_layer_sizes = tuple( [ self.n_hidden for i in range(self.n_layers) ] )
        self.hidden_layer_sizes = hidden_layer_sizes
        
        del params["n_hidden"]
        del params["n_layers"]
        
        super().set_params(**params)
        
            
