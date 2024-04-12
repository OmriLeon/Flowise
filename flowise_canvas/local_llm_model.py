```python
class LLM_Model:
    def __init__(self, model_id):
        self.model_id = model_id
        self.model = None

    def load_model(self):
        try:
            with open(f'{self.model_id}.pkl', 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            print(f"Model with ID {self.model_id} not found.")
            return None

        return self.model

    def predict(self, input_data):
        if self.model is None:
            print("Model not loaded.")
            return None

        return self.model.predict(input_data)
```