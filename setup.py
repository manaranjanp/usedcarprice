import setuptools

setuptools.setup(
    name='usedcarprice',
    version='0.0.1',
    author='Manaranjan Pradhan',
    author_email='manaranjan@gmail.com',
    description='Predicting the price of an used car',
    url='https://github.com/manaranjanp/usedcarprice',
    license='MIT',
    packages=['usedcarprice'],
    install_requires=['xgboost>=0.90', 'scikit-learn>=0.22.2']
)
