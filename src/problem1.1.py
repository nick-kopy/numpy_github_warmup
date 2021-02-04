import numpy as np

def border_with_zeros(arr):
    '''
    Takes in a 2D numpy array and adds
    a border of zeros around the outer edge

    Example:

        arr = np.array([
            [1,1],
            [1,1]
        ])
        border_with_zeros(arr)

    Would return:

        np.array([
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ])
    '''
    # your code here!
    arrx = arr.shape[0] + 2
    arry = arr.shape[1] + 2
    arrs = (arrx, arry)
    output = np.zeros(arrs)
    output[1:-1, 1:-1] = arr
    return output

if __name__ == '__main__':
    # Test your code here!
    arr = np.array([
        [1,1,1],
        [1,1,1]
    ])
    print(border_with_zeros(arr))
