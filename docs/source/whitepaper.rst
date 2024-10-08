Dynamic Shuffled Keyboard Stream Cipher for Encryption
===========================================================

:Author: Andrew R. Garcia
:Contact: garcia.gtr@gmail.com

Abstract
-----------

The algorithm presented in this paper, ``STREAMDICE``, is a novel stream cipher that provides encryption by considering the specific identity of characters and their relative location in the message string. ``STREAMDICE`` utilizes dynamically shuffled keyboards, generated by a cryptographically secure pseudo-random number generator (CSPRNG), with each keyboard shifted for every encrypted character. These shuffled keyboards are stored in memory using securely derived seeds, dependent on the provided encryption keys. This approach optimizes auxiliary space complexity while enhancing resistance to brute force attacks. The decryption process reverses the encryption protocol using the same keys.

Introduction
---------------

Effective encryption is crucial for protecting data and private information. Proper encryption ensures that unauthorized access to data is meaningless without the correct encryption keys. The algorithm presented here, ``STREAMDICE``, is a stream cipher that encrypts characters (i.e., letters, numbers, and some allowed signs) by their specific identity and their relative location in the message string thread. ``STREAMDICE`` uses dynamically shuffled keyboards generated by a cryptographically secure pseudo-random number generator (CSPRNG), with each keyboard shifted for every encrypted character. This method obfuscates periodicity and enhances resistance to brute force attacks, making it a robust encryption solution.

Related Work
---------------

Stream ciphers like RC4, ChaCha20, and Snow 3G are widely used, employing Linear Feedback Shift Registers (LFSRs) or similar mechanisms to generate keystreams. Modern approaches focus on lightweight designs for IoT, GPU implementations for high-speed encryption, and hybrid methods combining chaos theory and stream ciphers for enhanced security and performance. ``STREAMDICE`` introduces a novel method by using dynamically shuffled keyboards, providing a new layer of randomness and complexity.

Method
--------

Unwarped Map Creation
^^^^^^^^^^^^^^^^^^^^^^^

The unwarped map represents the original arrangement of characters on a QWERTY keyboard, including uppercase and lowercase letters, numbers, and special characters. Let :math:`\mathbb{C}` be the character set used for encryption. The bidirectional map, :math:`p_U`, associates each character :math:`\mathcal{C}_i \in \mathbb{C}` with its corresponding index :math:`i`:

.. math::

    p_U = \{ (\mathcal{C}_i, i) \, | \, \forall i \, (\mathcal{C}_i \in \mathbb{C}) \}
    p_U^{-1} = \{ (i, \mathcal{C}_i) \, | \, \forall i \, (i \in \mathbb{N}) \}

.. figure:: ../img/keyboard.png
   :align: center
   :width: 70%

   Standard QWERTY keyboard

Map Warping
^^^^^^^^^^^^^

The map warping operation :math:`p_W` is initialized with a :math:`\text{CSPRNG}(\mu_i)` seeding, where :math:`\mu_i` is a seed generated by the encryption key provided by the user. This operation reshuffles the keys, adding a layer of randomness to the encryption process. Every map warping operation produces a unique keyboard set.

.. figure:: ../img/hash5443.png
   :align: center
   :width: 70%

   Randomly-shuffled keyboard with \( \mu_i \) seed #5443

Character Encryption and Decryption Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The encryption process transforms input characters :math:`\mathcal{S}_i` into their corresponding encrypted characters :math:`\mathcal{C}_i` using :math:`p_W` map warping. Decryption reverses this process using :math:`p_U` map unwarping. For each character :math:`\mathcal{S}_i` in a message string :math:`\mathbb{S}`, the algorithm retrieves the corresponding index using :math:`p_U(\mathcal{S}_i)` and applies :math:`p_W` to obtain :math:`\mathcal{C}_i`. If :math:`\mathcal{S}_i` is a space, it is directly printed.

Security Analysis
-------------------

``STREAMDICE`` leverages cryptographically secure PRNGs and strong key derivation functions to generate seeds, ensuring robustness against brute force and cryptographic attacks. The dynamic shuffling of keyboards for each character encryption introduces high entropy, obfuscating periodicity and enhancing security.

Conclusion
------------

``STREAMDICE`` introduces a novel approach to stream ciphers by employing dynamically shuffled keyboards and secure seed management. This method optimizes memory usage while providing robust security against brute force attacks. Future work will focus on formal security proofs and performance optimizations.
