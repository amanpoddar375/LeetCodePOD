## Algorithm

1. If the number of element in array <= 3, then all those trees will fall on the edge of the fence.

2. Sort the array based on the x-axis values.

3. Create UpperConvexHull list as upper and insert the first two sorted element in them.

4. Then we compute the angle, the 3rd point is created with these two point

        a. If it is counterclockwise (crossProduct) Z > 0, we pop the list and inset the present element.
  
        b. else we add the present element to the list.

5. Create the LowerConvexHull list as lower and insert the last two sorted elements in them.

6. Follow the step 4. But traverse backward.

7. Merge the upper and lower list and remove the duplicates.

8. Return the Mergedlist.
