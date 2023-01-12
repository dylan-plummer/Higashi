from setuptools import setup, find_packages
print (find_packages())
setup(
    name='higashi',
    version='0.1.0a0',
    description='Higashi: Multiscale and integrative scHi-C analysis',
    url='https://github.com/ma-compbio/Higashi',
    include_package_data=True,
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=[
        'numpy,
        'scipy',
        'pandas4',
        'cython',
        'torch',
        'fbpca',
        'scikit-learn',
        'tqdm',
        'h5py',
        'cooler',
        'seaborn',
        'umap-learn',
        'Pillow'
    ],
    extras_require={},
    author='Ruochi Zhang',
    author_email='ruochiz@andrew.cmu.edu',
    license='MIT'
)

