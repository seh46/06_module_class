class numberInfo(object):
    """This is a class that provides information about numerical lists.

    __init__ sets the list attribute

    Attributes:
        myList (list or tuple input)
        maxDiff (max difference between 2 consecutive elements)
        sumList (sum of the elements)
        minMax (minimum and maximum of the list)
    """

    def __init__(self, input_list):
        self.myList = input_list
        self.maxDiff = None
        self.sumList = None
        self.minMax = None

    def max_diff(self):
        """Function to find the maximum magnitude difference between
        consecutive elements in a numerical list

        :param self object with a myList attribute

        :return: attribute with maximum magnitude consecutive difference as a
        scalar, or a vector if equal maximum difference in positive negative
        directions

        :rtype: scalar or array

        :raises ValueError: if the numerical list input is of length less than
        2
        :raises TypeError: if a non-numerical list is given
        :raises ImportError: if a required package was not loaded
        """
        import logging

        diff_var = []
        try:
            for i in range(0, len(self.myList) - 1):
                diff_var.append(self.myList[i + 1] - self.myList[i])

            if abs(max(diff_var)) > abs(min(diff_var)):
                max_diff = max(diff_var)
            elif abs(max(diff_var)) < abs(min(diff_var)):
                max_diff = min(diff_var)
            elif max(diff_var) == min(diff_var):
                max_diff = max(diff_var)
            else:
                max_diff = [min(diff_var), max(diff_var)]
            logging.info('Function completed without errors')

        except ValueError:
            print('Numerical list must be at least of length 2')
            logging.warning('Found max diff is of type None')
            max_diff = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Found max diff is of type None')
            max_diff = None
        except ImportError:
            # This file does not use any non-standard python packages like
            # numpy
            print('Missing package... or basic python installation')
            logging.debug('Required package is not installed')
            max_diff = None

        self.maxDiff = max_diff

    def sum_list(self):
        """Find the sum of all elements in a list

        :param  self object with a myList attribute

        :return: attribute with sum of list elements

        :raises ValueError: if infinity is in the input array
        :raises TypeError: if list is empty or contains non-numerical elements
        :raises ImportError: if a required package was not loaded
        """
        import logging
        import numpy as np

        try:
            if float('inf') in self.myList or float('-inf') in self.myList:
                raise ValueError
            if len(self.myList) == 0:
                raise TypeError
            my_sum = np.sum(self.myList)
            logging.info('Function completed without errors')

        except ImportError:
            print('Missing Numpy')
            logging.debug('numpy is not installed')
            my_sum = None
        except TypeError:
            print('Only numerical lists are accepted')
            logging.warning('sum is None')
            my_sum = None
        except ValueError:
            print('Input contains inappropriate value')
            logging.warning('sum is None')
            my_sum = None

        self.sumList = my_sum

    def min_max(self):
        """Finds the minimum and maximum values of a numerical list.

        :param self object with a myList attribute

        :returns: attribute with minimum and maximum values of list
        
        :raises ImportError: if numpy is not installed
        :raises TypeError: if a non-numerical list is given
        """
        import logging
        import numpy as np

        try:
            min_val = np.amin(self.myList)
            max_val = np.amax(self.myList)
            min_max_out = (min_val, max_val)
            logging.info('Function was completed successfully.')

        except ImportError:
            print('Missing package: numpy')
            logging.debug('Required package numpy is not installed')
            min_max_out = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Min/max is not numerical list')
            min_max_out = None
        except ValueError:
            print('Numerical list must be at least of length 1')
            logging.warning('Min/max is not of length 1 or greater')
            min_max_out = None

        self.minMax = min_max_out
