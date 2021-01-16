from distutils.core import setup


setup(
    name="torweave",
    packages=["torweave"],
    version="0.1.0",
    description="privacy protocol built on the blockweave",
    url="https://github.com/permaleaks/torweave",
    author="permaleaksMan",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8"
		"Programming Language :: Python :: 3.9.1",

    ],

    include_package_data=True,
    install_requires=[
        "jwcrypto", "bs4", "arweave-python-client", "Crypto", "base64",
    ]
)