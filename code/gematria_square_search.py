import pandas as pd
import pdb
import os

# Usage: python3 gematria_square_search.py
# Write file "all_found.tsv" to the current directory

topdir = "%s/lp_experiments" % os.environ['HOME']
datadir = "%s/data" % topdir


def combine_matrices():
    """
    Combines the numbers in matrices one and two into a set of unique numbers
    """
    matrix_dict = {}
    matrix_one = pd.read_csv('%s/matrix_1_numbers_only.csv' % datadir, header=None)
    matrix_two = pd.read_csv('%s/matrix_2.csv' % datadir, header=None)
    matrix_one_vals = matrix_one.values.flatten()
    for v in matrix_one_vals:
        if v not in matrix_dict:
            matrix_dict[v] = 1
    matrix_two_vals = matrix_two.values.flatten()
    for v in matrix_two_vals:
        if v not in matrix_dict:
            matrix_dict[v] = 2
    combined = set(matrix_two_vals).union(set(matrix_one_vals))
    return combined, matrix_dict


def make_dict(fp, grouped_col):
    """
    Creates a dictionary whose keys are gematria sums and whose values
    are words or sentences of the solved Liber Primus (depending on the
    grouped_col parameter
    """
    gematria_df = pd.read_csv(fp)
    gematria_df['translated'] = "(" + gematria_df['translated'] + ")"
    gematria_df['combined'] = gematria_df[grouped_col].str.cat(gematria_df.translated, ' ')
    grouped = gematria_df.groupby('gematria_sum')
    with_arrays = grouped.combined.apply(list).reset_index()
    as_dict = {}
    for s, array in with_arrays[['gematria_sum', 'combined']].values:
        as_dict[s] = array
    return as_dict


def do_search(numbers, dict_list):
    """
    Looks for all the numbers in a numbers list in a list of dictionaries
    Returns another dictionary consisting of the results of the search.
    """
    found_dict = {}
    for n in numbers:
        found_dict[n] = []
        for my_dict in dict_list:
            if n in my_dict:
                vals = my_dict[n]
                found_dict[n] = vals + found_dict[n]
        if len(found_dict[n]) == 0:
            found_dict[n].append("not found")
    return found_dict


def make_dataframe(found_dict, matrix_dict):
    """
    Turns the results of a search into a dataframe, though because the data is
    semi-structured, it is a little awkward.
    """
    numbers = []
    strings = []
    matrix_codes = []
    for k, v in found_dict.items():
        v = ', '.join(v)
        strings.append(v)
        numbers.append(k)
        matrix_codes.append(matrix_dict[k])
    res = pd.DataFrame({'numbers': numbers, 'strings': strings, 'matrix': matrix_codes})
    res = res.sort_values(by=['matrix'], axis=0)
    res = res.set_index(pd.Index(range(res.shape[0])))
    return res


def main():
    """
    Looks for the numbers in the magic squares in gematria values of the 
    words and sentences of the solved Liber Primus.
    """
    words_dict = make_dict('%s/words_solved.csv' % datadir, 'word')
    sentences_dict = make_dict('%s/sentences_solved.csv' % datadir, 'sentence')
    matrix_nums, matrix_dict = combine_matrices()
    found_dict = do_search(matrix_nums, [words_dict, sentences_dict])
    df = make_dataframe(found_dict, matrix_dict)
    df.to_csv('all_found.tsv', sep='\t', index=False)


if __name__ == "__main__":
    main()
