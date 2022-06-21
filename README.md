# StreamDice

StreamDice is a C++ program running on a unique [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) developed by Andrew Garcia based on the constant random shuffling of keyboard maps. 

### Contributing

StreamDice welcomes contributions to the StreamDice project. An effort should be made in closing security vulnerabilities while keeping the cipher algorithm stable, that is, one should make an effort to keep the ciphertext conventions constant. 

### Usage

#### Input Commands
```ruby
./streamdice [ key ] [ encrypt[1]/decrypt[0] ]
```
#### Example

##### encryption
```bash
./streamdice 7412369 1
enter message:
Hello World. Hello again!
--- message encrypted! ---
CT*lX @yKlW- 0Rl+X Bnp=Uo
```
##### decryption
```bash
./streamdice 7412369 0
enter message:
CT*lX @yKlW- 0Rl+X Bnp=Uo
--- message deciphered! ---
Hello World. Hello again!
```

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

