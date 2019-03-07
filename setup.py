from setuptools import setup

setup(
    name='captcha_solver',
    version='0.1',
    packages=['captcha_solver'],
    url='https://github.com/prikid/captcha_solver_demo',
    license='',
    author='Serhii Riabcheniuk',
    author_email='serhii@prikid.app',
    description='Captcha solver',
    install_requires=[
        'numpy',
        'opencv-python',
        'imutils',
        'pytesseract'
    ],

)
