# streamdice

streamdice is a [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) developed by Andrew Garcia based on the catalogued random shuffling of keyboard hashmaps.

A cipher is an encryption algorithm and thus, can be applied to program development in
any language. [**Streamdice**](./streamdice) and [**streamdiceJS**](./streamdiceJS) are the C++ and web (JavaScript) implementations of this cipher, respectively.

| [Read the white paper](https://github.com/andrewrgarcia/streamdice/blob/main/whitepaper.pdf) |
| -------------------------------------------------------------------------------------------- |

| [Check out the online demo](https://andrewatcloud.com/streamdice/) |
| ------------------------------------------------------------------ |

### Contributions Welcome / Hacktoberfest

Meaningful contributions to the project are always welcome. Participating in Hacktoberfest 2022. Before making a PR, please make sure to read the [CONTRIBUTING](./CONTRIBUTING.md) document.

You may use the Issues section of this repository if you'd like to propose some new ideas/enhancements or report a bug.

### Disclaimer: Use At Your Own Risk

This program is free software. It comes without any warranty, to the extent permitted by applicable law. You can redistribute it and/or modify it under the terms of the MIT LICENSE, as published by Andrew Garcia. See [LICENSE](https://github.com/andrewrgarcia/streamdice/blob/main/LICENSE) for more details.

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

**[MIT license](./LICENSE)** Copyright 2022 © <a href="https://github.com/andrewrgarcia" target="_blank">Andrew Garcia</a>.

```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```
