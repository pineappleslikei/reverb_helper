import ez_gsheets as ezg

# change ss_id to be the id of your google sheet
ss_id = '1ldymz7Oe_hE7C6y6aKVJ065FuMe7-el1Mt2TLTyK2SI'


def main():
    sheet = ezg.get_gsheet(ss_id)
    rows = sheet.getRows()
    for row in rows[1:]:
        if row[2] != '':
            links = ezg.check_for_links(row)
            row = ezg.put_link(row, links)
    sheet.updateRows(rows)


if __name__ == "__main__":
    main()
