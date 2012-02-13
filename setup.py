from setuptools import setup, find_packages
 
setup(
    name='pycrop',
    version='0.9',
    description='Crops and resizes to produce a square thumbnail ',
    author='CondeNet, Inc / christopherhan',
    # author_email='',
    url='https://github.com/christopherhan/pycrop',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
