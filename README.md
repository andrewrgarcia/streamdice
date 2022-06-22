# StreamDice

StreamDice is a C++ program running on a unique [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) developed by Andrew Garcia based on the constant random shuffling of keyboard maps. 

### Contributing

StreamDice welcomes contributions to the StreamDice project. An effort should be made in closing security vulnerabilities while keeping the cipher algorithm stable, that is, one should make an effort to keep the ciphertext conventions constant. 

### Disclaimer: Use At Your Own Risk
This program is free software. It comes without any warranty, to the extent permitted by applicable law. You can redistribute it and/or modify it under the terms of the MIT LICENSE, as published by Andrew Garcia. See [LICENSE](https://github.com/andrewrgarcia/streamdice/blob/main/LICENSE) for more details.

### Usage 

#### encryption
```bash
./streamdice 145 145236 1
enter message:
Hello World. Hello again! olleH (5 letters) is 'Hello' backwards.
--- message encrypted! ---
I4tY# 7#CYYC {2Y$S sv`yjG 1Y$BI Br nE&yW[ti ,v VI4tY#V ];~IrO.5vQ
```
#### decryption
```bash
./streamdice 145 145236 0
enter message:
I4tY# 7#CYYC {2Y$S sv`yjG 1Y$BI Br nE&yW[ti ,v VI4tY#V ];~IrO.5vQ
--- message deciphered! ---
Hello World. Hello again! olleH (5 letters) is 'Hello' backwards.
```
### Details
```ruby
// Input command format
./streamdice [ key1 ] [ key2 ] [ encrypt[1]/decrypt[0] ]  %

// Inputs
[ key1 ]    type long;   range:   0 to 2147483647  // "keep it shorter than 10 digits"
[ key2 ]    type long;   range:   1 to (2147483647 or < message_size)
[ encrypt ] type int;    range:   1 or 0 (True or False)

// Characters not supported:
\  ? | "
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

