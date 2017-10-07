def H2H(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_H2H""" + year + """](
	[ID] [int] NOT NULL,
	[IFLTNR] [nvarchar](10) NULL,
	[IDATE] [datetime] NULL,
	[IFLTINFOID] [int] NULL,
	[IORIGIN] [nvarchar](3) NULL,
	[ISTAND] [nvarchar](5) NULL,
	[IETA] [datetime] NULL,
	[IATA] [datetime] NULL,
	[HULLOPEN] [datetime] NULL,
	[IUNLOAD] [decimal](5, 1) NULL,
	[ITAXI] [decimal](5, 1) NULL,
	[IINJECT] [decimal](5, 1) NULL,
	[ETU] [datetime] NULL,
	[INRBAGS] [int] NULL,
	[ONTOFLIGHT] [nvarchar](10) NULL,
	[HUB] [int] NULL,
	[OFLTNR] [nvarchar](10) NULL,
	[ODATE] [datetime] NULL,
	[OFLTINFOID] [int] NULL,
	[OLNRBAGS] [int] NULL,
	[OINJECT] [decimal](5, 1) NULL,
	[OTAXI] [decimal](5, 1) NULL,
	[OLOAD] [decimal](5, 1) NULL,
	[ETL] [datetime] NULL,
	[ETLU] [datetime] NULL,
	[ETD] [datetime] NULL,
	[HULLCLOSE] [datetime] NULL,
	[ATD] [datetime] NULL,
	[STANDD] [nvarchar](5) NULL,
	[CR] [nvarchar](1) NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_H2H""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID] 
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [IFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IDATE]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT (NULL) FOR [IFLTINFOID]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [IORIGIN]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [ISTAND]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IETA]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IATA]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [HULLOPEN]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [IUNLOAD]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [ITAXI]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [IINJECT]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETU]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [INRBAGS]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [ONTOFLIGHT]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [HUB]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [OFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ODATE]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT (NULL) FOR [OFLTINFOID]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [OLNRBAGS]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [OINJECT]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [OTAXI]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [OLOAD]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETL]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETLU]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETD]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [HULLCLOSE]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ATD]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [STANDD]
ALTER TABLE [dbo].[OSUSR_UUK_H2H""" + year + """] ADD  DEFAULT ('') FOR [CR]

"""
    return create