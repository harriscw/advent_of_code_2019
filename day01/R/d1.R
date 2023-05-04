rm(list=ls())
input=as.numeric(readLines("../advent.txt"))

print(paste("Part 1",sum(floor((input/3)-2))))

### Part 2
### Do part 2 as a while loop

fuelval=function(x){ #helper function to do calc on last element, input is a vector
  return(floor(tail(x,1)/3)-2)
}

acc=c()
for(i in input){ #iterate over each val
  newval=c()
  x=fuelval(tail(i,1)) #set initial fuel value
  while(x>0){ #don't stop until 0 or negative
    newval=c(newval,x) #append to vector of fuel needs
    x=fuelval(tail(newval,1)) #reset values
  }
  acc=c(acc,sum(newval)) #sum them when its done
}

print(paste("Part 2",sum(acc)))


### Do part 2 as a recursive function

fuelval_recurse=function(x){ #input is a vector, do calc on last element
  if(fuelval(x)>0){ #if the fuel at the last element >=0
    x=c(x,fuelval(x)) #append it to the list
    fuelval_recurse(x) #and keep going
  }else{ #...otherwise you've reached the end so return the vector
    return(x[-1]) #removing the initial input from recursive function result
  }
}

acc=sapply(input,function(val){ #iterate over input, apply recursive function, append sum to vector
  sum(fuelval_recurse(val))
},simplify = TRUE)

print(paste("Part 2",sum(acc)))

