Sqlite Index
============

Installing
----------
Install and update using `pip` :

.. code-block:: text
  
  $ pip install sqlite-index
 
..

Example
-------
Here is a quick example to using `sqlite-index`

.. code-block:: python

  from sqlite_index import Index
  import os
  
  basedir = os.path.dirname(os.path.abspath(__file__))
  
  # Where the data is stored
  products_filename = os.path.join(basedir, "products")
  
  # Index instance
  PRODUCTS_INDEX = Index(products_filename, _fields=["title", "description"])

  data = [

      {
          "title" : "Roku Streaming Stick+ | HD/4K/HDR Streaming Device with Long-range Wireless and Voice Remote with TV Controls",
          "description" : """Wireless that goes the distance: Basement rec room? Backyard movie night? Bring ‘em on. 
                              The long-range wireless receiver gives you extended range and a stronger signal for 
                              smooth streaming even in rooms farther from your router
                              Brilliant picture quality: Experience your favorite shows with stunning detail and 
                              clarity—whether you’re streaming in HD, 4K, or HDR, you’ll enjoy picture quality 
                              that’s optimized for your TV with sharp resolution and vivid color"""
      },

      {
          "title" : "Dell SE2419Hx 24\" IPS Full HD (1920x1080) Monitor, Black",
          "description" : """Thin bezel
                              1920 x 1080 at 60 hertz full HD maximum resolution
                              16:9 aspect ratio
                              Compact base to maximize desk space
                              1000:1 contrast ratio. Brightness: 250 Candela per square meter (TYP)
                              60 hertz"""
      },

      {
          "title" : "Acer R240HY bidx 23.8-Inch IPS HDMI DVI VGA (1920 x 1080) Widescreen Monitor, Black",
          "description" : """23.8" Full HD IPS widescreen with 1920 x 1080 resolution
                              Response time: 4ms, refresh rate: 60 hertz, pixel pitch: 0.2745 millimeter. 
                              178 degree wide viewing angle, display colors: 16.7 million
                              The zero frame design provides maximum visibility of the screen from edge to edge
                              Signal inputs: 1 x HDMI, 1 x DVI (withHDCP) & 1 x VGA. Does not support HDCP 2.2, 
                              the version this monitor supports is HDCP 1.4
                              No picture visible using the OSD menu, adjust brightness and contrast to maximum or 
                              reset to their default settings. Brightness is 250 nit. Operating power consumption: 25 watts"""
      },

      {
          "title" : "SAMSUNG 970 EVO Plus SSD 2TB - M.2 NVMe Interface Internal Solid State Drive with V-NAND Technology (MZ-V7S2T0B/AM)",
          "description" : """NNOVATIVE V-NAND TECHNOLOGY: Powered by Samsung V-NAND Technology, the 970 EVO Plus SSD’s NVMe 
                              interface (PCIe Gen 3.0 x4 NVMe 1.3) offers enhanced bandwidth, low latency, and power efficiency ideal for tech enthusiasts, 
                              high end gamers, and 4K & 3D content designers
                              BREAKTHROUGH READ WRITE SPEEDS: Sequential read and write performance levels of up to 3,500MB/s and 3,300MB/s, 
                              respectively; Random Read (4KB, QD32): Up to 600,000 IOPS Random Read
                              PERFORMANCE OPTIMIZATION AND DATA SECURITY: Seamless cloning and file transfers with Samsung Magician Software, 
                              the ideal SSD management solution for performance optimization and data security with automatic firmware updates"""
      }
  ]

  for idx, item  in enumerate(data):
      title, description = item["title"], item["description"]

      # Adding data to Index
      PRODUCTS_INDEX.add(
          title,
          idx,
          ["title"] # Section of the database it'll be added to
      )

      PRODUCTS_INDEX.add(
          description,
          idx,
          ["description"]
      )

  # Search Index

  print( PRODUCTS_INDEX.search("with", ["description"]))
  
  # outputs:
  # search function took 0.000 ms
  # [0, 2, 3]
  
  # To seach the title
  # print( PRODUCTS_INDEX.search("with", ["title"]))
  # However you can put all fields to search the whole index
  # i.e PRODUCTS_INDEX.search("with", ["title", "description"])
..

To remove data from Index
-------------------------

.. code-block:: python

  # To remove data from index
  PRODUCTS_INDEX.remove(
          description,
          idx,
          ["description"]
  )

..
