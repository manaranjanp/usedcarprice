import setuptools

setuptools.setup(
    name='usedcar',
    version='0.2.0',
    author='Manaranjan Pradhan',
    author_email='manaranjan@gmail.com',
    description='Predicting the price of an used car',
    url='https://github.com/manaranjanp/usedcarprice',
    license='MIT',
    packages=['usedcar'],
    include_package_data=True,
    install_requires=['xgboost>=0.90', 'scikit-learn>=0.22.2']
)
