from distutils.core import setup


setup(
    name='modulo_vki',
    version='0.2',
    description="MODULO (MODal mULtiscale pOd) is a software developed at the von Karman Institute to perform Multiscale Modal Analysis of numerical and experimental data using the Multiscale Proper Orthogonal Decomposition (mPOD).",
    long_description=open('README.rst', 'rt').read(),
    author="L. Schena",
    author_email='lorenzoschena@vki.ac.be',
    url='https://github.com/lorenzoschena/modulo_vki',
    packages=['modulo',],
    include_package_data=True,
    package_data={
        'modulo': [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=open('requirements.txt', 'rt').read(),
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
