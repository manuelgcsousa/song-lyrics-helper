<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <meta charset="UTF-8"/>
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">jQuery</script>
				<script>
                    $(document).ready(function() {
                        $("#flip1").click(function() {
                            $("#panel1").slideToggle("slow");
                        });
                    });
                    
                    $(document).ready(function() {
                        $("#flip2").click(function() {
                            $("#panel2").slideToggle("slow");
                        });
                    });

					/*
                    $(document).ready(function() {
                        $("#flip3").click(function() {
                            $("#panel3").slideToggle("slow");
                        });
					});
					*/
                </script> 
                <style>
                    * {
                        font-family: Lucida Grande;
                    }
                    
                    table, tr {
                        border: 5px solid #4CAF50;
                        font-size: 15px;
                        background-color: #f2f2f2
                    }
                   	
                    #flip1 {
                        padding: 10px;
                        text-align: center;
                        background-color: #f2f2f2;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel1 {
                        padding: 10px;
                        text-align: left;
                        background-color: #FFFFFF;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel1 {
                        padding: 50px;
                        display: none;
                    }
                    
                    #flip2 {
                        padding: 10px;
                        text-align: center;
                        background-color: #f2f2f2;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel2 {
                        padding: 10px;
                        text-align: left;
                        background-color: #FFFFFF;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel2 {
                        padding: 50px;
                        display: none;
                    }

					/*
                    #flip3 {
                        padding: 10px;
                        text-align: center;
                        background-color: #f2f2f2;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel3 {
                        padding: 10px;
                        text-align: left;
                        background-color: #FFFFFF;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel3 {
                        padding: 50px;
                        display: none;
					}
					*/
                </style>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>
	
    <xsl:template match="meta">
        <h1 align="center">Palavra: <xsl:value-of select="word"/></h1>
    </xsl:template>

	<xsl:template match="rhymes">
        <div id="flip1"><b>RIMAS</b></div>
        <div id="panel1">
            <ul>
                <xsl:apply-templates/>
            </ul>
            <br/>
            <hr/>
        </div>
        <br/>
    </xsl:template>
    
	<xsl:template match="syl">
		<li>
			<b><xsl:value-of select="@n"/> Sílabas</b>
			<ul>
				<xsl:apply-templates/>
			</ul>
		</li>
		<br/>
    </xsl:template>
	
	<xsl:template match="rhyme">
		<li>
			<xsl:value-of select="."/>
		</li>
	</xsl:template>

	<xsl:template match="similars">
		<div id="flip2"><b>PALAVRAS SIMILARES</b></div>
        <div id="panel2">
            <ul>
                <xsl:apply-templates/>
            </ul>
            <br/>
            <hr/>
        </div>
        <br/>
	</xsl:template>

	<xsl:template match="similar">
		<li>
			<xsl:value-of select="."/>
		</li>
	</xsl:template>
</xsl:stylesheet>
