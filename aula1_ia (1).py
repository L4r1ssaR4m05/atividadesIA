# -*- coding: utf-8 -*-
"""aula1_IA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ug9pBtfWxHI0ffKuMVze4KDoUZW_WYVw

Primeiro modelo GAN de IA. É utilizado para aprendizado de máquina para gerar novos dados semelhantes a um conjunto de dados de treinamento.
"""

#importando as bibliotecas q eu vo ultilizar

import tensorflow as tf
from tensorflow.keras import layers

#função para criar um gerador
def build_generator(latent_dim, output_shape):
  model = tf.keras.Sequential()
  model.add(layers.Dense(256,input_dim=latent_dim,activation='relu'))
  model.add(layers.BatchNormalization())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.BatchNormalization())
  model.add(layers.Dense(1024, activation='relu'))
  model.add(layers.BatchNormalization())
  model.add(layers.Dense(output_shape, activation='tanh'))
  return model

#função para criar o discriminador
def build_discriminator(input_shape):
  model = tf.keras.Sequential()
  model.app(layers.Dense(1024,input_shape=(input_shape,), activation='relu'))
  model.add(layers.Dropout(0.3))
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dropout(0.3))
  model.add(layers.Dense(256, activation='relu'))
  model.add(layers.Dropout(0.3))
  model.add(layers.Dense(1, activation='sigmoid'))
  return model

#fução modelo gan
def build_gan(generator, discriminator):
  discriminator.trainable = False
  model = tf.keras.Sequential()
  model.add(generator)
  model.add(discriminator)
  return model

  #dimenções
  latent_dim = 100
  output_shape = 784

  #criando as instâncias
  generator = build_generator(latent_dim, output_shape)
  discriminator = build_discriminator(output_shape)
  gan = build_gan(genarator, discriminator)

  #compilações
  generator.compile(loss='binary_crossentropy', optimizer='adam')
  discriminator.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
  gan.compile(loss='binary_crossentropy', optimizer='adam')

"""Este codigo uma vez treinadas pode gerar novas que parecem pertencer ao mesmo conjunto de dados que foi usado para treinamento, como imagens que se assemelham a digitos manuscritos (por exemplo, MNIST)."""