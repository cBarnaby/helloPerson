#include <iostream>
#include <string>

class person{
    std::string title, firstName, lastName;
    int age;

    public:
        person(std::string title, std::string firstName, std::string lastName, int age) {
            this->title = title;
            this->firstName = firstName;
            this->lastName = lastName;
            this->age = age;
        }

        void greetInformal() {
            std::cout << "Hello, " << this->title << " " << this->lastName << "!\n";
        }

        void greetFormal() {
            std::cout << "Hello, " <<this->title << " " <<this->lastName << "!\n";
        }

        void howOld() {
            std::cout <<this->firstName << " is " <<this->age << " years old.\n";
        }

        void birthday() {
            this->age += 1;
            std::cout << "Happy Birthday, " << this->firstName << "! You are now " << this->age << " years old.\n";
        }
};

int main() {
    std::string title, firstName, lastName;
    int age;

    std::cout << "What is your title? ";
    std::cin >> title;
    std::cout << "What is your first name? ";
    std::cin >> firstName;
    std::cout << "What is your last name? ";
    std::cin >> lastName;
    std::cout << "How old are you? ";
    std::cin >> age;

    person you(title, firstName, lastName, age);

    you.greetInformal();
    you.greetFormal();
    you.howOld();
    you.birthday();
    you.howOld();

    return 0;
}
