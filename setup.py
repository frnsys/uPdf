from setuptools import setup

setup(
    name='updf',
    version='0.0.2.4',
    description='Tool for manipulating PDFs',
    author='Lorenzo Carbonell Cerezo',
    author_email='lorenzo.carbonell.cerezo@gmail.com',
    license='GPLv3',
    zip_safe=True,
    package_data={'updf': ['data/**/*']},
    include_package_data=True,
    packages=['updf'],
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        updf=updf.updf:main
    ''',
)
