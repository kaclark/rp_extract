# Content-based Organization and Visualization of Music Archives

## ABSTRACT  

With Islands of Music we present a system which facilitates exploration of music libraries without requiring man-  ual genre classification. Given pieces of music in raw audio  format we estimate their perceived sound similarities based  on psychoacoustic models. Subsequently, the pieces are or-  ganized on a 2-dimensional map so that similar pieces are  located close to each other. A visualization using a metaphor  of geographic maps provides an intuitive interface where is-  lands resemble genres or styles of music. We demonstrate  the approach using a collection of 359 pieces of music.

## Introduction 

Large music archives, such as those of online music retailers, 
usually offer several ways to find a desired piece of music. 
A straightforward approach is to use text based queries to 
search for the artist, the title or some phrase in the lyrics. 
Although such queries are very efficient they do not offer any 
particular support for queries based on the perceived simi- 
larities of music. For example, a simple text query asking for 
pieces with characteristics similar to F¨ur Elise by Beethoven 
would return pieces with either the same title or the same 
artist. Thus, pieces like Fremde L¨ander und Menschen by 
Schumann would be ignored.

The common solution is to organize music collections by a hierarchical structure of predefined genres and styles such as Classical, Jazz, Rock. Hence, a customer seeking something similar to F¨ur Elise can limit the search to all pieces in the same category. However, such organizations rely on manual categorizations and usually consist of several hundred categories and sub-categories which involve high maintenance costs, in particular for dynamic collections. The difficulties of such taxonomies have been analyzed, for example, in [19].

Another approach, taken by online music stores is to analyze 
the behavior of customers to give those showing similar in- 
terests recommendations on music which they might appre- 
ciate. For example, a simple approach is to give a customer 
looking for pieces similar to F¨ur Elise recommendations on 
music which is usually bought by people who also purchased 
F¨ur Elise. However, extensive and detailed customer profiles 
are rarely available

The Islands of Music system we propose facilitates explo-  ration of music archives without relying on further infor-  mation such as customer profiles or predefined categories.  Instead, we estimate the perceived sound similarities be-  tween two pieces of music and organize them in such a way  that similar pieces of music are close to each other on a 2-  dimensional map display. We visualize this organization us-  ing a metaphor of geographic maps where islands represent  musical genres or styles and the arrangement of the islands  reflects the inherent structure of the music collection

The main challenge is to calculate an estimation for the per-  ceived similarity of two pieces of music. To achieve this, we  use audio data as it is available from CD or decoded MP3  files. The raw audio signals are preprocessed in order to ob-  tain a time-invariant representation of the perceived char-  acteristics following psychoacoustic models. In particular,  we extract features which characterize dynamic properties  of the music, namely rhythm patterns.

To cluster and organize the pieces on a 2-dimensional map  display we use the Self-Organizing Map [12], a prominent  unsupervised neural network. This results in a map where  similar pieces of music are grouped together. In addition  we visualize clusters using Smoothed Data Histograms [21]  to simplify the identification of interesting regions on the  map and to obtain the island visualization. We demonstrate  the user interface using a collection of 359 popular pieces of  music resembling a wide spectrum of musical taste.

The remainder of this paper is organized as follows. Section 2 briefly reviews related work. The novel feature extraction process is presented in Section 3, followed by the organization and visualization of the music archives, which  is presented in Section 4. We give a brief discussion of the  user interface in Section 5 and present experiments in Sec-  tion 6. Finally, in Section 7 some conclusions are drawn. 
