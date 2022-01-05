#!/usr/bin/env python3

genres = {
    "fantasy": "Usually set in a fictional imagined world with prominent elements of magic, mythology or the supernatural.",
    "romance": "The genre that makes your heart all warm and fuzzy focuses on the love story of the main protagonists.",
    "classics": "The classics have been around for decades, and were often groundbreaking stories at their publish time, but have continued to be impactful for generations, serving as the foundation for many popular works we read today.",
    "horror": "Meant to cause discomfort and fear for both the character and readers, horror writers often make use of supernatural and paranormal elements in morbid stories that are sometimes a little too realistic.",
    "mystery": "The plot always revolves around a crime of sorts that must be solved—or foiled—by the protagonists.",
}


def main():
    genre = input(
        "Please enter the following options to learn more about he genre: Fantasy, Romance, Classics, Horror, Mystery: \n --> "
    ).lower()

    if genre in genres:
        print(genres[genre])
    else:
        print("You did not enter a valid input. Please try again")
        print("")
        main()


main()
