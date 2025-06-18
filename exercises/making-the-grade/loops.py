"""Functions for organizing and calculating student exam scores."""

from typing import List


def round_scores(student_scores: List[float]) -> List[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[float]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failing_student_count = sum(1 for score in student_scores if score <= 40)
    return failing_student_count


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> List[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    boundary_interval = round((highest - 40) / 4)
    return [boundary for boundary in range(41, highest, boundary_interval)]


def student_ranking(student_scores: List[int], student_names: List[int]):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    complete_scores: List[str] = []
    for pointer in range(0, len(student_scores)):
        complete_scores.append(f"{pointer + 1}. {student_names[pointer]}: {student_scores[pointer]}")

    return complete_scores


def perfect_score(student_info: List[List[str]]) -> List[str]:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student_details in student_info:
        if student_details[1] == 100:
            return student_details

    return []
