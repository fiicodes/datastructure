def getSecondOrderElements(n: int, a: [int]) -> [int]:
    def findsecondlarge(a, n):
        largest = a[0]
        secondlarge = -1
        for i in range(1, n):
            if a[i] > largest:
                secondlarge = largest
                largest = a[i]
            elif a[i] < largest and a[i] > secondlarge:
                secondlarge = a[i]
        return secondlarge

    def findsecondsmallest(a, n):
        smallest = a[0]
        secondsmallest = float("inf")
        for i in range(1, n):
            if a[i] < smallest:
                secondsmallest = smallest
                smallest = a[i]
            elif a[i] !=smallest and a[i] < secondsmallest:
                secondsmallest = a[i]
        return secondsmallest

    secondlargest = findsecondlarge(a, n)
    secondsmallest = findsecondsmallest(a, n)
    return [secondlargest, secondsmallest]

    # Write your code here.
