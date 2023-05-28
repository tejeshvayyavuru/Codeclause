from difflib import SequenceMatcher
import textwrap
import colorama
from colorama import Fore, Style


def calculate_similarity(text1, text2, method='levenshtein'):
    """Calculates the similarity between two texts using different methods."""
    if method == 'levenshtein':
        return levenshtein_similarity(text1, text2)
    elif method == 'sequence_matcher':
        return sequence_matcher_similarity(text1, text2)
    else:
        raise ValueError(f"Unsupported method: {method}")


def levenshtein_similarity(text1, text2):
    """Calculates the similarity between two texts using Levenshtein distance."""
    m = len(text1)
    n = len(text2)

    # Initialize a matrix with dimensions (m+1) x (n+1)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    # Calculate the minimum edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if text1[i - 1] == text2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # deletion
                matrix[i][j - 1] + 1,      # insertion
                matrix[i - 1][j - 1] + cost  # substitution
            )

    # Calculate similarity score
    similarity = 1 - (matrix[m][n] / max(m, n))
    return similarity


def sequence_matcher_similarity(text1, text2):
    """Calculates the similarity between two texts using SequenceMatcher."""
    matcher = SequenceMatcher(None, text1, text2)
    similarity = matcher.ratio()
    return similarity


def check_plagiarism(text1, text2, method='levenshtein', threshold=0.8):
    """Checks if two texts are plagiarized based on a similarity threshold."""
    similarity = calculate_similarity(text1, text2, method)
    if similarity >= threshold:
        print(Fore.RED + "Plagiarism detected!")
        print(f"Similarity score: {similarity:.2f}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "No plagiarism detected.")
        print(f"Similarity score: {similarity:.2f}" + Style.RESET_ALL)


def format_text(text, width=80):
    """Formats the text into multiple lines with the specified width."""
    return textwrap.fill(text, width)


def get_user_input(prompt):
    """Gets user input with the provided prompt."""
    try:
        return input(prompt)
    except EOFError:
        print()  # Print a newline for better formatting
        return ""


def print_title(title):
    """Prints a formatted title for the plagiarism checker."""
    print("=" * 40)
    print(f"{Fore.CYAN}{title}{Style.RESET_ALL}")
    print("=" * 40)


# Main function
def main():
    # Initialize colorama
    colorama.init()

    print_title("Plagiarism Checker")

    while True:
        print("\nPlease enter the two texts for plagiarism comparison:")
        text1 = get_user_input("Text 1: ")
        text2 = get_user_input("Text 2: ")

        if not text1 or not text2:
            print("Invalid input. Please try again.")
            continue

        method = get_user_input("\nEnter the similarity calculation method (levenshtein/sequence_matcher): ")
        threshold = float(get_user_input("Enter the similarity threshold (0-1): "))

        print("\nChecking plagiarism...")
        check_plagiarism(format_text(text1), format_text(text2), method=method, threshold=threshold)

        choice = get_user_input("\nDo you want to check plagiarism again? (y/n): ")
        if choice.lower() != 'y':
            break

    print("\nThank you for using the Plagiarism Checker!")
    colorama.deinit()


# Run the main function
if __name__ == '__main__':
    main()