In the previous folder, we tryed to findout the avarage of the slopes. but that was not matched with the actual result get from scikit learn.
Now we takes the avarage x and y coordinates of each datapoint. and findout the distance between from each x to the mean of x and y to the mean of y.
we know y/x is the slope. so y-something/x-something is also a slope. but if we multiply x and y and devide it with the squre of x, the it will be also another kind of slope. and this is the same slope we got from scikit learn.
Now we know the slope of the trend and we have multple points, so we can easily find the bias with the eqution y=mx + b.
