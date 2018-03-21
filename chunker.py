import hashlib
import fastchunking
import string


def chunk(text_str: str,min_chunk_size=20)->list:
    size_of_roling_chunk=5
    chunks=[]
    cdc = fastchunking.RabinKarpCDC(window_size=24, seed=0)
    chunker = cdc.create_chunker(chunk_size=100)
    #Add the start position as initial boundary
    chunk_boundaries=[0]+chunker.next_chunk_boundaries(text_str)
    chunk_boundaries.append(len(text_str))

    for boundary_index in range (1,len(chunk_boundaries)):
        start=chunk_boundaries[boundary_index-1]
        stop=chunk_boundaries[boundary_index]
        print("Chunk size =",stop-start)
        chunk_size=stop-start
        if chunk_size<min_chunk_size:
            chunk_boundaries[boundary_index]=chunk_boundaries[boundary_index-1]
            continue
        chunk=text_str[start:stop]
        chunks.append(chunk)
    if not chunks:
        chunks=[text_str]
    return(chunks)

 
def normalize(text_str: str,remove_whitespace=True,lowercase=True,remove_punctuation=True,extra_remove_chars=[])->str:
    if remove_whitespace:
        text_str=''.join(text_str.split())
    if lowercase:
        text_str=text_str.lower()
    if remove_punctuation:
        for char in string.punctuation:
            text_str=text_str.replace(char,'')
    for char in extra_remove_chars:
        text_str=text_str.replace(char,'')
    return text_str

def hash(text_str: str)->str:
    return hashlib.md5(text_str.encode('utf8')).hexdigest()

def main():
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc consectetur, \
    elit eu suscipit imperdiet, odio tortor efficitur augue, sed auctor magna libero \
    ut nisl. In lacinia, elit quis feugiat auctor, nulla mi efficitur justo, nec volutpat \
    leo nulla maximus metus. Aenean tempor gravida purus quis suscipit. Nulla facilisi. \
    Aenean pharetra nunc nisi. Nunc auctor quam tellus, sagittis gravida mauris tincidunt \
    quis. In pellentesque nulla a ligula venenatis, eget egestas metus fringilla. Nunc quis \
    velit nisl. Cras et lectus placerat, placerat massa id, volutpat sapien. Vestibulum sed \
    ultrices ipsum, vel blandit dolor. Suspendisse viverra enim eget ligula facilisis, sed \
    interdum ante consectetur. Suspendisse faucibus eleifend laoreet."
    print(chunk(normalize(text)))

if __name__ == "__main__":
    main()