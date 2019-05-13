import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
from mnist_dataset import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)

print(t_train.shape)

print(x_test.shape)

print(t_test.shape)