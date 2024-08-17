Usage
=====

.. _installation:

streamdice.py
----------------
Andrew Garcia, 2021

Oldest implementation of streamdice algorithm. Written in Python

* Encrypts all characters, including spaces. 

* Requires 1 key as an input, but  the root block and SEQUENCE block of the streamdice algorithm are preserved. 

make app.sh executable with  ``chmod +x app.sh`` and run

.. code-block:: console

   cd pystreamdice
   chmod +x app.sh
   ./app.sh        // input command



streamdice ("streamdice++")
--------------------------------------

C++ implementation to streamdice 

Usage 
.............

Silent Keys (with app.sh)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Command line in *streamdice/* directory:

make app.sh executable with  `chmod +x app.sh`

Encryption

.. code-block:: console

   cd streamdice
   ./app.sh 1  // input command

>>> [OUT]
enter key #1:
enter key #2:
enter message:
Hello World. Hello again! olleH (5 letters) is 'Hello' backwards.
--- message encrypted! ---
I4tY# 7#CYYC {2Y$S sv`yjG 1Y$BI Br nE&yW[ti ,v VI4tY#V ];~IrO.5vQ


Decryption

.. code-block:: console

   cd streamdice
   ./app.sh 0  // input command

>>> [OUT]
enter key #1:
enter key #2:
enter message:
I4tY# 7#CYYC {2Y$S sv`yjG 1Y$BI Br nE&yW[ti ,v VI4tY#V ];~IrO.5vQ
--- message encrypted! ---
Hello World. Hello again! olleH (5 letters) is 'Hello' backwards.


Explicit Keys (with direct ./streamdice)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Command line in *streamdice/build/* directory:

.. code-block:: console

   ./streamdice 145 145236 1        // input command for encryption
   enter message:

   ./streamdice 145 145236 0		// input command for decryption
   enter message:

Details 
..................

.. code-block:: console

   // Input command format
   ./streamdice [ key1 ] [ key2 ] [ encrypt[1]/decrypt[0] ]  %

   // Inputs
   [ key1 ]    type long;   range:   0 to 2147483647  // "keep it shorter than 10 digits"
   [ key2 ]    type long;   range:   1 to (2147483647 or < message_size)
   [ encrypt ] type int;    range:   1 or 0 (True or False)

   // Characters not supported:
   \  ? | "
   ```
   
Usage password/generator.cpp
...................................


**Klang it!** Install klang (https://github.com/andrewrgarcia/klang)

.. code-block:: console

   cd password
   klang generator.cpp
   ./generator.k


Installation Quick Start
...............................

A basic installation template.


Installing Boost
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   ##### Linux

   apt-get install -y libboost-iostreams-dev

   ##### macOS
   brew install boost
   ##### Windows

   vcpkg install boost-iostreams:x64-windows
   vcpkg install boost-any:x64-windows
   vcpkg install boost-algorithm:x64-windows
   vcpkg install boost-uuid:x64-windows
   vcpkg install boost-interprocess:x64-windows


Building StreamDice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   git clone git@github.com: ...
   cd streamdice/streamdice; mkdir build; cd build; cmake ..; cmake --build .

streamdiceJS
------------------


streamdiceJS is the interactive web [JavaScript] implementation of the StreamDice cipher. 

Usage
...........

web-ready 
^^^^^^^^^^^^^^^

Check out our `online demo <https://streamdice.vercel.app/>`_

Local computer
^^^^^^^^^^^^^^^

.. code-block:: console

   cd streamdiceJS
   npm run build

Then apply dist/main.js to web
