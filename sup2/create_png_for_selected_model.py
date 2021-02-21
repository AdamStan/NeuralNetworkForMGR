import keras


best_model = keras.models.load_model("model-the-best.h5")
best_model_score = keras.models.load_model("model-the-best-score.h5")
best_model_acc = keras.models.load_model("model-the-best-accuracy.h5")

keras.utils.plot_model(best_model, to_file="model_the_best.png", show_shapes=True)
keras.utils.plot_model(best_model_score, to_file="model_the_best_score.png", show_shapes=True)
keras.utils.plot_model(best_model_acc, to_file="model_the_best_accuracy.png", show_shapes=True)
