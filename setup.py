from setuptools import setup, Extension

setup(
    name='example_pkg',
    version='0.0.1',
    description='An basic python package example',
    author='Sam Hadden',
    author_email='shadden1107@gmail.com',
    license='GPL',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['numpy','scipy>=1.2.0']
)
