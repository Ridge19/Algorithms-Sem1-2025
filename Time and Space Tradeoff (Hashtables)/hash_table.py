class Entry:
    """
    Inner class representing a cell.
    """
    def __init__(self, newKey=None, newValue=None):
        self.key = newKey
        self.value = newValue

"""
* Hash table implementation using linear probing for collision.
"""
class HashTable:
    def __init__(self, size, max_load_factor):
        """
        *  Create the hash table.
        *  
        *  @param size Initial size of hash table.
        *  @param max_load_factor Maximum load factor before we self.rehash.       
        """
        self.table = [None]*size
        self.item_num = 0
        self.max_load_factor = max_load_factor

    def calc_hash(self, key):
        """
        *  This is the hash function.   Implement as described in the lab sheet.
        *  
        *  @param key Key to hash.
        *  
        *  @return Hash value of key.       
        """
        hash_val = 0        

        # IMPLEMENT ME

        return hash_val

    def insert(self, key, value):
        """
        *  Insert into hash table and self.rehash if loadfactor too high.
        *  
        *  @param key Key to insert.
        *  @param value Associated value.        
        """

        # self.rehash if too full 
        if  self.item_num / len(self.table) > self.max_load_factor:
            self.rehash()

        # IMPLEMENT ME


    def delete(self, key):
        """
        *  Delete a key + value pair from the hash table.
        *  
        *  @param key Key to delete.       
        """
        # IMPLEMENT ME


    def lookup(self, key):
        """
        *  Check for membership of a key.
        *  
        *  @param key Key to search.
        *  
        *  @return Associated value, or null if key not in table.       
        """
        # IMPLEMENT ME

        # dummy placeholder
        return None


    def rehash(self):
        """
        Resize the hash table so the load factor is ''normal'' again.
        """
        # calc new hash table size based on load factor 
        new_size = self.item_num * 4 # 25 % full 
        old_table = [None]*len(self.table)
        old_table[:len(self.table)] = self.table
        self.table = [None]*new_size

        # self.rehash the values on the old hash table 
        for i in range(len(old_table)):
            if old_table[i] != None:
                self.insert(old_table[i].key, old_table[i].value)


    def __str__(self):
        """
        *  Returns the list of key-value pairs in table.
        *  
        *  @return of the list of key-vallue pairs.       
        """
        output_str = ""
        # output all key + value pairs 
        output_str += "key" + "\t\t" + "value\n"
        for i in range(len(self.table)):
            if self.table[i] != None:
                output_str += f"{self.table[i].key}\t\t{self.table[i].value}\n"
        
        return output_str
