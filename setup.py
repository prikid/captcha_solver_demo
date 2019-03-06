from setuptools import setup, find_packages

setup(
    name='captcha_solver',
    version='1.0',
    packages=['captcha_solver'],
    url='prikid.app',
    license='',
    author='Serhii Riabcheniuk',
    author_email='serhii@prikid.app',
    description='',
    install_requires=[
        'numpy',
        'cv2',
        'imutils',
        'pytesseract'
    ],

)
