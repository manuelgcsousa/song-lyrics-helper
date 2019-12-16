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
                        $("#flip").click(function() {
                            $("#panel").slideToggle("slow");
                        });
                    });
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
                   	
                    #flip {
                        padding: 10px;
                        text-align: center;
                        background-color: #f2f2f2;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel {
                        padding: 10px;
                        text-align: left;
                        background-color: #FFFFFF;
                        border: solid 4px #4CAF50;
                    }
                    
                    #panel {
                        padding: 50px;
                        display: none;
                    }
                </style>
            </head>
            <body>
                <h1 align="center">Lista de Sugestões</h1>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>
	
    <xsl:template match="meta">
        <h3 align="center">Língua: <xsl:value-of select="lang"/></h3>
    </xsl:template>

	<xsl:template match="words">
        <div id="flip"><b>LISTA DE PALAVRAS</b></div>
        <div id="panel">
            <ul>
                <xsl:apply-templates/>
            </ul>
            <br/>
            <hr/>
        </div>
        <br/>
    </xsl:template>
    
	<xsl:template match="word">
		<li>
			<a href="./words/{.}.html"><xsl:value-of select="."/></a>
		</li>
		<br/>
    </xsl:template>
</xsl:stylesheet>
