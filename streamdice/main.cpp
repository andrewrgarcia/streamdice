// StreamDice++
// A message-encryption C++ program made by Andrew Garcia based
// on a unique stream cipher also developed by Andrew, ``StreamDice'', based on the
// constant random shuffling of keyboard character hashmaps.
//
// github: https://github.com/andrewrgarcia/streamdice
// Andrew Garcia, 2022
#include <iostream>
#include <string>
// #include <unordered_map>
#include <boost/bimap.hpp>
#include <bits/stdc++.h>

void printvector(std::vector<int> vector)
{
    for (int k = 0; k < vector.size(); k++)
    {
        printf("%d ",
               vector[k]);
    }
}

boost::bimap<boost::bimaps::set_of<std::string>,
             boost::bimaps::set_of<int>>
unwarped_map()
{
    std::string qwerty{"QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`1234567890-=~!@#$%^&*()_+[];',./{}:<>"};
    std::vector<int> charord;

    typedef boost::bimap<boost::bimaps::set_of<std::string>,
                         boost::bimaps::set_of<int>>
        bimap;
    bimap umap;

    for (int i = 0; i < 90; i++)
    {
        std::string str(1, qwerty[i]); // char to str
        umap.insert({str, i});
    }
    return umap;
}

boost::bimap<boost::bimaps::set_of<int>,
             boost::bimaps::set_of<std::string>>
map_warping(int device)
{
    std::string qwerty{"QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`1234567890-=~!@#$%^&*()_+[];',./{}:<>"};
    std::vector<int> charord;

    typedef boost::bimap<boost::bimaps::set_of<int>,
                         boost::bimaps::set_of<std::string>>
        bimap;
    bimap umap;

    for (int i = 0; i < 90; i++)
        charord.push_back(i);

    std::mt19937 generator(device);

    std::shuffle(charord.begin(), charord.end(), generator);

    int k = 0;
    for (int i : charord)
    {
        std::string str(1, qwerty[k]); // char to str
        umap.insert({i, str});
        k++;
    }

    return umap;
}

void scribe(std::string msg_frac, long root, long spawn, bool &encrypt)
{

    std::mt19937 generator(root);
    int dev = generator() + spawn;

    boost::bimap<boost::bimaps::set_of<std::string>,
                 boost::bimaps::set_of<int>>
        umap0{unwarped_map()};

    boost::bimap<boost::bimaps::set_of<int>,
                 boost::bimaps::set_of<std::string>>
        umap{map_warping(dev)};

    for (auto x : msg_frac)
    {
        std::string s(1, x); // char to str
        if (s == " ")
            std::cout << " ";
        else
        {
            if (encrypt)
                std::cout << umap.left.at(umap0.left.at(s));
            else
                std::cout << umap0.right.at(umap.right.at(s));
        }
    }
}

void machine(std::string message, long key1, long key2, bool encrypt)
{
    long root{key1};
    std::vector<int> sequence;

    int i = 0;
    while (key2 > 0)
    {
        int digit = key2 % 10;
        key2 /= 10;
        sequence.push_back(digit);
        i++;
    }

    if (encrypt)
        printf("--- message encrypted! ---\n");
    else
        printf("--- message deciphered! ---\n");

    i = 0;
    for (auto k : message)
    {
        std::string s(1, k); // char to str
        scribe(s, root, sequence[i], encrypt);
        i++;
        i %= sequence.size();
    }
    printf("\n");
}

int main(int argc, char **argv)
{
    // std::string message{argv[1]};
    long key{std::stol(argv[1])};
    long key2{std::stol(argv[2])};
    int encrypt{std::stoi(argv[3])};
    std::string message;

    // printf("encrypt or decrypt?\nencrypt: 1; decrypt: 0;\n");
    // scanf("%d", &encrypt);

    // if (encrypt)
    //     std::cout << "enter message to encrypt:" << std::endl;
    // else
    //     std::cout << "enter message to decrypt:" << std::endl;

    // printf("enter key:\n");
    // scanf(" %d", &key);
    //
    std::cout << "enter message:" << std::endl;
    std::getline(std::cin >> std::ws, message);

    machine(message, key, key2, encrypt);
}
