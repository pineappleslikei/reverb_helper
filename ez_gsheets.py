import ezsheets as ez
import google_drive as g
import url_format as uf


def get_gsheet(spreadsheet_id):
    # change ss_id to be the id of your google sheet
    ss_id = spreadsheet_id
    # instantiate Spreadsheet object
    ss = ez.Spreadsheet(ss_id)
    sheet = ss[0]
    # index for rows makes sure column title don't get processed
    rows = sheet.getRows()[1:]
    return sheet


def check_for_links(row):
    if row[1] == 'TRUE':
        if row[15] == '':
            links = g.google_processing(row[2])
            new_links = [uf.url_pipe(link) for link in links]
            return new_links
        else:
            print('Already has links')


def put_link(row, links):
    num_links = len(links)
    if num_links > 0:
        i = 14 + int(num_links)
        for link in links:
            row[i] = link
            i -= 1
    return row
