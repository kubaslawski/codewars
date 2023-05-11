/*
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

 */

Array.prototype.sameStructureAs = function (other) {
    if (!Array.isArray(this) || !Array.isArray(other)){
        return false;
    }
    if(this.length !== other.length){
        return false;
    }
    for(let i=0; i<this.length; i++){
        if(Array.isArray(this[i]) !== Array.isArray(other[i])){
            return false;
        }
        if(Array.isArray(this[i]) && Array.isArray(other[i])){
            if(!this[i].sameStructureAs(other[i])){
                return false;
            }
        }
    }
    return true;

};
