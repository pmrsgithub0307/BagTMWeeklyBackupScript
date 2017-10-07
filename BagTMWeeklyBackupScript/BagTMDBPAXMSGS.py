def PAXMSGS(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """](
	[ID] [int] NOT NULL,
	[IFLTNR] [nvarchar](10) NULL,
	[IDATE] [datetime] NULL,
	[IORIGIN] [nvarchar](3) NULL,
	[OFLTNR] [nvarchar](10) NULL,
	[ODATE] [datetime] NULL,
	[ODEST] [nvarchar](3) NULL,
	[FIRST] [int] NULL,
	[BUSINESS] [int] NULL,
	[ECONOMY] [int] NULL,
	[INF] [int] NULL,
	[CHD] [int] NULL,
	[RESERVATIONSTATUS] [nvarchar](2) NULL,
	[TIMESTAMP] [datetime] NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_PAXMSGS""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID] 
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('') FOR [IFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IDATE]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('') FOR [IORIGIN]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('') FOR [OFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ODATE]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('') FOR [ODEST]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [FIRST]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [BUSINESS]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [ECONOMY]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [INF]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [CHD]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('') FOR [RESERVATIONSTATUS]
ALTER TABLE [dbo].[OSUSR_UUK_PAXMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [TIMESTAMP]

"""
    return create