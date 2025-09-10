def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    """
    Splits the input text into chunks of specified size with a given overlap.

    Parameters:
    text (str): The input text to be chunked.
    chunk_size (int): The maximum size of each chunk.
    overlap (int): The number of overlapping characters between consecutive chunks.

    Returns:
    List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = (text[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

        if start < 0:
            start = 0
    return chunks


def chunked_summarize(text: str, summarize_func, max_chunk_size: int = 2000) -> str:
        """
        Summarizes a long text by breaking it into chunks, summarizing each chunk,
        and then combining the summaries.

        Parameters:
        text (str): The input text to be summarized.
        summarize_func (Callable[[str], str]): A function that takes a string and returns its summary.
        max_chunk_size (int): The maximum size of each chunk for summarization.

        Returns:
        str: The combined summary of the input text.
        """

        # Step 1: Chunk the text
        text_chunks = chunk_text(text, chunk_size=max_chunk_size, overlap=200)

        # Step 2: Summarize each chunk
        partial_summaries = [summarize_func(chunk) for chunk in text_chunks]

        # Step 3: Combine the partial summaries
        combined_summary_input = " ".join(partial_summaries)

        # Step 4: Final summarization of the combined summaries
        final_summary = summarize_func(combined_summary_input)

        return final_summary
