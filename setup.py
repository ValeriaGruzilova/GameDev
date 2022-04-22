import setuptools
from sphinx.setup_command import BuildDoc

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

cmdclass = {'build_sphinx': BuildDoc}
name = 'Magic Rush'
version = '0.0.2'

setuptools.setup(
    name=name,
    version=version,
    cmdclass=cmdclass,
    author='Valeria Gruzilova',
    description='single-player arcade game for pc',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Valery-Gruzilova/GameDev',
    license='MIT',
    keywords='pc game GameDev Magic Rush arcade magicrush',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/build')
        }
    }
)