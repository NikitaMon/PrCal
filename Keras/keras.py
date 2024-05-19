import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf

from tensorflow.python.keras.models import Sequential       # основной класс для последовательного соединения слоёв
from tensorflow.python.keras.layers import Dense, Input         # полносвязный слой (каждый нейрон в этом слое будет соединён с каждым в соседнем)
from tensorflow.python.keras.layers import Flatten
from keras import metrics                 # метрики качества

from tensorflow.python.keras.optimizers import adam_v2    # класс для подбора параметров нейросети (модификация градиентного пуска)
from tensorflow.python.keras.utils.np_utils import to_categorical    # для one-hot кодирования

from tensorflow.python.keras.engine import data_adapter

def _is_distributed_dataset(ds):
    return isinstance(ds, data_adapter.input_lib.DistributedDatasetSpec)

data_adapter._is_distributed_dataset = _is_distributed_dataset


# ========================================
import keras
import matplotlib.pyplot as plt
# загрузка датасета
tf.keras.datasets.mnist.load_data(path="mnist.npz")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
y_train = tf.keras.utils.to_categorical(y_train)
plt.imshow( x_train[0] )
#=========================================

model = Sequential()     

model.add( Flatten(input_shape=(28,28)) )
model.add(  Dense(100, input_dim = 4, activation='sigmoid')  ) # первый слой (не считая входного)
                                                          # 10 -- число нейронов
                                                          # input_dim=4 -- число входов для каждого нейрона = число признаков
                                                          # activation='relu' -- функция активации
# model.add ???

model.add( Dense(10, activation='sigmoid') )              # выходной слой. число входов каждого нейрона расчитвыается автоматически. 
                                                          # оно равно числу нейронов в предыдущем слое
                                                          # каждый из трёх нейронов этого слоя отвечает за узнавание своего класса и выдаёт число от 0 до 1 (активация -- сигмоида)

opt =   adam_v2.Adam(learning_rate=0.01)                            # объект для подбора параметров модели градиентным спуском
                                                          # learning_rate -- коэффициент шага изменения параметров нейросети
# большой шаг -- быстрое обучение, но грубый подбор параметров
# маленький шаг -- медленное обучение, но точный подбор параметров

# завершающий этап созданий нейросети
model.compile(loss='categorical_crossentropy',            # функция потерь
              optimizer=opt,                            
            #   metrics=[metrics.Accuracy()]                # метрики, которые нужно вычислять в конце каждой эпохи
              metrics=['accuracy']                # метрики, которые нужно вычислять в конце каждой эпохи
              )                       

model.build( input_shape = (768,) )

model.summary()   # выводит на экран информацию о сети

#exit()

# =======================
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))


# далее применение и обучение модели
with tf.device('/device:GPU:0'):
    # обучение
    model.fit(x_train, y_train, 
            epochs=600,                     # число эпох -- число прогонов всей обучающей выборки
            batch_size=x_train.shape[0],    # размер одной порции данных (батча), после которой будут меняться коэффициенты
                                            # здесь зададим размер равный всей обучающей выборке
            )

# лучше выбирать максимально возможный размер батча, т.е. такой который помещается в оперативную память
# но если один проход обучения занимает млишком много времени и трудно контролировать переобучение,
# то размер стоит уменьшить

#============================

# предсказания (сразу для массива объектов - картинок)
y_pred = model(x_test)

#============================
# преобразования из one-hot encoding в число
# например
# [1,0,0,0,0, 0,0,0,0,0] -> 0
# [0,1,0,0,0, 0,0,0,0,0] -> 1
# [0,0,1,0,0, 0,0,0,0,0] -> 2
# ...
# [0,0,0,0,0, 0,0,0,0,1] -> 9

y_pred_labels = tf.argmax(y_pred, axis=1)           # axis -- вдоль какой размерности записан one-hot массив?

#============================


from sklearn.metrics import classification_report

# отчёт о классификации
print( classification_report(y_test, y_pred_labels ) )
# accuracy - обща точность (среди всех классов)
# https://scikit-learn.org/stable/modules/model_evaluation.html#classification-report

#=============================