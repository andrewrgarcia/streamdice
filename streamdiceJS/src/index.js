// streamdiceJS
// Andrew Garcia, 2022
// A web (JavaScript) version of Andrew Garcia's `streamdice` stream-cipher algorithm 
// streamdice is based on the catalogued random shuffling of keyboard hashmaps. 
import BiMap from 'bimap';
import Swal from 'sweetalert2';

function mulberry32(a) {
  return function () {
    var t = a += 0x6D2B79F5;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  }
}


function shuffle(array, generator) {
  // adapted from https://stackoverflow.com/questions/521295/seeding-the-random-number-generator-in-javascript
  var m = array.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(generator() * m--);

    // And swap it with the current element.
    t = array[m];
    array[m] = array[i];
    array[i] = t;
  }

  return array;
}


function unwarped_map() {

  var umap = new BiMap;
  const qwerty = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`1234567890-=~!@#$%^&*()_+[];',./{}:<>";


  for (let i = 0; i < 90; i++) {
    umap.push(qwerty[i], i);
  }
  return umap;
}



function map_warping(device) {

  var umap = new BiMap;
  const qwerty = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`1234567890-=~!@#$%^&*()_+[];',./{}:<>";

  var charord = [];

  for (let i = 0; i < 90; i++) {
    charord.push(i);
  }

  var generator = mulberry32(device);
  var charord = shuffle(charord, generator);

  for (let i = 0; i < 90; i++) {
    umap.push(charord[i], qwerty[i]);
  }

  return umap;
}

function scribe(msg_frac, root, spawn, encrypt) {

  var generator = mulberry32(root);

  var dev = generator() + spawn;

  var umap0 = unwarped_map();
  var umap = map_warping(dev);

  var msg_trans = []
  for (let i = 0; i < msg_frac.length; i++) {
    var s = msg_frac[i];

    if (s == " ") {
      var letter = " "

    } else {

      if (encrypt == 1) {
        var letter = umap.key(umap0.key(s));
      } else {
        var letter = umap0.val(umap.val(s));
      }
    }

    msg_trans.push(letter);
  }
  return msg_trans;

}

function machine(message, key1, key2, encrypt) {

  var root = key1;
  var num = key2;
  var digits_str = num.toString();
  var digits = digits_str.split('');
  var sequence = digits.map(Number)

  var new_message = [];
  var i = sequence.length;
  for (let k = 0; k < message.length; k++) {
    var s = message[k]
    new_message.push(scribe(s, root, sequence[i], encrypt));
    i--; // iterate from last to first in `key2` ; analogous to reverse digit chain in c++
  }

  return new_message.join('');
}


async function app() {

  // const { value: encrypt } = await Swal.fire({
  //   title: 'Welcome to streamdiceJS!',
  //   input: 'text',
  //   inputLabel: 'Encrypt [1]; Decipher [0]',
  //   inputPlaceholder: 'Enter "1" to encrypt OR "0" to decipher message',
  //   inputAttributes: {
  //     maxlength: 10,
  //     autocapitalize: 'off',
  //     autocorrect: 'off'
  //   }
  // })

  const inputOptions = new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        1: 'Encrypt',
        0: 'Decipher',
      })
    }, 1000)
  })
  
  const { value: encrypt } = await Swal.fire({
    title: 'Welcome to streamdiceJS!',
    input: 'radio',
    inputOptions: inputOptions,
    // inputValidator: (value) => {
    //   if (!value) {
    //     return 'You need to choose something!'
    //   }
    // }
  })
  
  // if (color) {
  //   Swal.fire({ html: `You selected: ${color}` })
  // }


  const { value: key1 } = await Swal.fire({
    title: 'Enter Key #1',
    input: 'password',
    footer: 'Key #1 may be any number from 0 to 2147483647 <br><br>Recommendation: Keep your keys secure ',
    inputLabel: 'Password',
    inputPlaceholder: 'Enter your password',
    inputAttributes: {
      maxlength: 10,
      autocapitalize: 'off',
      autocorrect: 'off'
    }
  })



  const { value: key2 } = await Swal.fire({
    title: 'Enter Key #2',
    input: 'password',
    footer: 'Key #2 may be any number from 1 to ( 2147483647 or < message_length ) <br><br>Recommendation: Keep your keys secure ',
    inputLabel: 'Password',
    inputPlaceholder: 'Enter your password',
    inputAttributes: {
      maxlength: 10,
      autocapitalize: 'off',
      autocorrect: 'off'
    }
  })


  const { value: message } = await Swal.fire({
    input: 'textarea',
    inputLabel: 'Let`s encrypt / decipher your message',
    footer: 'Recommendation: Always test the encryption by running the deciphering of the encrypted message.',
    inputPlaceholder: 'Type your message here...',
    inputAttributes: {
      'aria-label': 'Type your message here'
    },
    // showCancelButton: true
  })



  if (encrypt == 1) {
    var encr = "--- message encrypted ---\n\n";
  } else {
    var encr = "--- message deciphered ---\n\n";
  }


  var newMessage = machine(message, key1, key2, encrypt);
  document.getElementById('log').innerHTML = encr + "<br><br>" + newMessage;


}


window.app = app;
// app()