import csv
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

RANDOM_SEED = 101
CLASSES = 4

X_dataset = np.loadtxt('training.csv', delimiter=',', dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
y_dataset = np.loadtxt('training.csv', delimiter=',', dtype='int32', usecols=(0))
X_train, X_test, y_train, y_test = train_test_split(X_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)
model = tf.keras.models.Sequential([
  tf.keras.layers.Input((21 * 2, )),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(20, activation='relu'),
  tf.keras.layers.Dropout(0.4),
  tf.keras.layers.Dense(10, activation='relu'),
  tf.keras.layers.Dense(CLASSES, activation='softmax')
])

es_callback = tf.keras.callbacks.EarlyStopping(patience=20, verbose=1)

model.compile(
  optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy']
)

model.fit(
  X_train,
  y_train,
  epochs=1000,
  batch_size=128,
  validation_data=(X_test, y_test),
  callbacks=[es_callback]
)
model.save('trained')

val_loss, val_acc = model.evaluate(X_test, y_test, batch_size=128)