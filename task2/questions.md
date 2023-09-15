## 2.3 What possible issues do you think you could run into if you were asked to extend the grammar considerably and how would you suggest overcoming them? There is no single correct response to this question so please share any potential issues that come to mind.

1. Ambiguity: As the grammar expands, there may be instances where sentences could have multiple interpretations. For example, the name of a song could also be the name of another band, and vice versa. To address this, we can utilize context, such as the user's request history. Additionally, real-world user interactions should be observed to identify ambiguities and improve the grammar overall.

2. Data Collection: Given the vast number of bands and singers, it can be challenging to include them all in the grammar to understand any music-related intent. To tackle this, we can employ web scraping techniques to collect data from public music sources. Furthermore, it is essential to explore existing artist databases for additional resources.

3. Performance: As the grammar grows in size, ensuring efficient performance becomes crucial. Large grammars might encounter performance issues, such as slower recognition times or increased memory requirements. To optimize the grammar, it is important to avoid repetitions and be mindful of optional elements.

## 2.4 Which features of your language complicate the localization or writing of the grammar? How would you solve or work around these complications?

1. Russian has highly inflectional morphology, particularly in nominals. Hence, careful consideration of different word forms for different intents is necessary. To handle this, we can leverage websites like [AOT](http://aot.ru/) or Python modules like `pymorphy2` to inflect words appropriately.

2. Russian word order is highly flexible, complicating the writing of the grammar rules. To address this issue, I suggest incorporating a "shuffle" operation into the grammar using curly brackets `{}`, indicating that elements within the brackets can be shuffled. By doing so, we can accommodate different word orders and reduce the chances of missing the recognition of certain utterances.

3. Adjectives in Russian have gender agreement, requiring us to choose the appropriate endings accordingly. Consider the following examples:

*play me something classic*

*play me some classic music*


In Russian, the first example should use the neutral gender "классическ***ое***", while the second example requires the feminine gender "классическ***ая***" (as "music" is feminine). The challenge here lies in considering different word forms based on the sentence structure in which they are used.
