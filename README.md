# StreamDice

StreamDice is a C++ program running on a unique [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) developed by Andrew Garcia based on the constant random shuffling of key maps with periodic random seeds. 

### Contributing

StreamDice welcomes contributions to the StreamDice project. An effort should be made in closing security vulnerabilities while keeping the cipher algorithm stable, that is, one should make an effort to keep the ciphertext conventions constant. 

### Quick Start

A basic installation template.

#### Installing Boost

##### Linux

```bash
apt-get install -y libboost-iostreams-dev
```
##### macOS
```bash
brew install boost
```
##### Windows

```
vcpkg install boost-iostreams:x64-windows
vcpkg install boost-any:x64-windows
vcpkg install boost-algorithm:x64-windows
vcpkg install boost-uuid:x64-windows
vcpkg install boost-interprocess:x64-windows
```


#### Building StreamDice
```bash
git clone git@github.com:....
cd streamdice
mkdir build
cd build
cmake ..
cmake --build .
```

